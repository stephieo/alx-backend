#!/usr/bin/node
import * as kue from 'kue';

// object with Job data

const jobData = {
  phoneNumber: '09087654321',
  message: 'this is a job',
};

// create queue
const push_notification_code = kue.createQueue();

// create Job

const job = push_notification_code.create('notification', jobData)
  .save((err) => {
    if (err) {
      console.log('Notification job creation failed: ', err);
    } else {
      console.log(`Notification job created: ${job.id}`);
    }
  });

// job event handler
job.on('complete', () => {
  console.log('Notification job completed');
}).on('failed', () => {
  console.log('Notification job failed');
});
