#!/usr/bin/node
import * as redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server', err);
});

const data = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

async function createHash(data) {
  for (const key in data) {
    if (data) {
      client.HSET('HolbertonSchools', key, data[key], redis.print);
    }
  }
  const getallAsync = promisify(client.HGETALL).bind(client);
  try {
    const output = await getallAsync('HolbertonSchools');
    console.log(JSON.stringify(output, null, 2));
  } catch (err) {
    console.log(err);
    throw err;
  }
}

createHash(data);
