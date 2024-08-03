#!/usr/bin/node
import * as kue from 'kue';

const push_notification_code_3 = kue.createQueue();

export default function createPushNotificationsJobs(jobs, push_notification_code_3) {
  if (Array.isArray(jobs) !== true) {
    throw Error('Jobs is not an array');
  }

  jobs.forEach((item) => {
    const job = push_notification_code_3.create('notification', item)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });
    job.on('complete', () => {
      console.log(`Notification job ${job.id} completed`);
    }).on('failed', (err) => {
      console.log(`Notification job ${job.id} failed: `, err);
    }).on('progress', (progress, data) => {
      console.log(`Notification job ${job.id} ${progress}% complete`);
    });
  });
}
