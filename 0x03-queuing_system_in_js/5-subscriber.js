#!/usr/bin/node
import * as redis from 'redis';

const subscriber = redis.createClient();

subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

subscriber.on('error', (err) => {
  console.log('Redis client not connected to the server: ', err);
});

// subcribe to channel
subscriber.subscribe('holberton school channel');

//  listen for incoming messages
subscriber.on('message', (channel, msg) => {
  if (msg === 'KILL_SERVER') {
    subscriber.unsubscribe(`${channel}`);
    subscriber.quit();
  }
  console.log(`${msg}`);
});
