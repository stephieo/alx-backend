#!/usr/bin/node
import * as kue from 'kue';

// create queue
const queue = kue.createQueue();

function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber} with message: ${message}`);
}

queue.process('notification', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});
