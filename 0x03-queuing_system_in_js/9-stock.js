#!/usr/bin/node
import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const listProducts = [
    {
	id: 1,
	name: 'Suitcase 250',
	price: 50,
	stock: 4,
    },
    {
	id: 2,
	name: 'Suitcase 450',
	price: 100,
	stock: 10,
    },
    {
	id: 3,
	name: 'Suitcase 650',
	price: 350,
	stock: 2,
    },
    {
	id: 4,
	name: 'Suitcase 1050',
	price: 550,
	stock: 5,
    },
];

function getItemById(id) {
    return listProducts.filter(item => item.id === id)[0];
}

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('error', (error) => {
    console.log(`Redis client not connected to the server: ${error.message}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

function reserveStockById(id, stock) {
    client.set(`item.${id}`, stock);
}

async function getCurrentReservedStockById(id) {
    const stock = await getAsync(`item.${id}`);
    return stock;
}

//express server
const app = express();
const port = 1245;

const notFound = { status: 'Product not found' };

app.listen(port, () => {
    console.log(`app listening at http://localhost:${port}`);
});

app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:id', async (req, res) => {
    const id = Number(req.params.id);
    const item = getItemById(id);

    if (!item) {
	res.json(notFound);
	return;
    }

    const currentStock = await getCurrentReservedStockById(id);
    const stock = currentStock !== null ? currentStock : item.stock;

    item.currentQuantity = stock;
    res.json(item);
});

app.get('/reserve_product/:id', async (req, res) => {
    const id = Number(req.params.id);
    const item = getItemById(id);
    const noStock = { status: 'Not enough stock available', id };
    const reservationConfirmed = { status: 'Reservation confirmed', id };

    if (!item) {
	res.json(notFound);
	return;
    }

    let currentStock = await getCurrentReservedStockById(id);
    if (currentStock === null) currentStock = item.stock;

    if (currentStock <= 0) {
	res.json(noStock);
	return;
    }

    reserveStockById(id, Number(currentStock) - 1);

    res.json(reservationConfirmed);
});