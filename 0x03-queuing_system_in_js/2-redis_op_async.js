#!/usr/bin/node
//  redis package exports using CommonJS.
//  Import the whole module and then destructure it:
import * as redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server', err);
});

function setNewSchool(schoolName, value) {
  client.SET(schoolName, value, redis.print);
}

const asyncRedisGet = promisify(client.GET).bind(client);
async function displaySchoolValue(schoolName) {
  const value = await asyncRedisGet(schoolName);
  console.log(value)
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco','100');
displaySchoolValue('HolbertonSanFrancisco');
