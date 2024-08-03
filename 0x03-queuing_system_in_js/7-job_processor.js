#!/usr/bin/node
import * as kue from 'kue';

const queue = kue.createQueue();

const blacklist = ['4153518780', '4153518780'];

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);
  if (blacklist.includes(phoneNumber)) {
   done(Error(`Phone number ${phoneNumber} is blacklisted`));
  } else {
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber} with message: ${message}`);
    done();
  }
}

queue.process('notification', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
})
