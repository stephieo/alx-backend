import express from 'express';
import { createClient } from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const client = createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const QUEUE_NAME = 'reserve_seat';
const port = 1245;
let reservationEnabled = true;

// Function to set available seats in Redis
const setAvailableSeats = async (number) => {
  await setAsync('available_seats', number);
};

// Function to retrieve the current number of available seats from Redis
const getAvailableSeats = async () => {
  const seats = await getAsync('available_seats');
  return seats ? parseInt(seats, 10) : 0;
};

// Initialize available seats
setAvailableSeats(50);

// Create job queue
const queue = kue.createQueue();

// Initialize Express app
const app = express();

// Endpoint to retrieve the number of available seats
app.get('/available_seats', async (req, res) => {
  const numberOfAvailableSeats = await getAvailableSeats();
  res.json({ numberOfAvailableSeats });
});

// Endpoint to create a reservation job
app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservations are blocked' });
    return;
  }

  const job = queue.create(QUEUE_NAME).save((err) => {
    if (err) {
      res.json({ status: 'Reservation failed' });
      return;
    }
    res.json({ status: 'Reservation in process' });
  });

  job.on('complete', () => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errMessage}`);
  });
});

// Endpoint to process reservation jobs
app.get('/process', (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process(QUEUE_NAME, async (job, done) => {
    const currentSeats = await getAvailableSeats();

    if (currentSeats <= 0) {
      reservationEnabled = false;
      return done(new Error('Not enough seats available'));
    }

    const newSeats = currentSeats - 1;
    await setAvailableSeats(newSeats);

    if (newSeats === 0) {
      reservationEnabled = false;
    }

    done();
  });
});

// Start server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
