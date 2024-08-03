#!/usr/bin/node

// TODO: Redo
import createPushNotificationsJobs from './8-job';
import kue from 'kue';
import { expect } from 'chai';

const testQueue = kue.createQueue();

const jobs = [
    {
	phoneNumber: '+24153518780',
	message: 'This is the code 1234 to verify your account',
    },
    {
	phoneNumber: '+25153118782',
	message: 'This is the code 38998 to verify your account',
    },
];

describe('createPushNotificationsJobs', () => {
    before(() => {
	testQueue.testMode.enter();
    });

    afterEach(() => {
	testQueue.testMode.clear();
    });

    after(() => {
	testQueue.testMode.exit();
    });

    it('throw a new error if jobs is not an array', () => {
	expect(() => {
	    createPushNotificationsJobs(2, testQueue);
	}).to.throw('Jobs is not an array');
    });

    it('throw a new error if jobs is not an array', () => {
	expect(() => {
	    createPushNotificationsJobs("wqfew", testQueue);
	}).to.throw('Jobs is not an array');
    });

    it('throw a new error if jobs is not an array', () => {
	expect(() => {
	    createPushNotificationsJobs({"Name": "ALX"}, testQueue);
	}).to.throw('Jobs is not an array');
    });

    it('Not throw any errors, return undefined', () => {
	const retValue = createPushNotificationsJobs([], testQueue);
	expect(retValue).to.equal(undefined);
    });

    it('Adds new jobs to the testQueue through the jobs array', () => {
	createPushNotificationsJobs(jobs, testQueue);
	expect(testQueue.testMode.jobs[0].type).to.equal('push_notification_code_3');

	expect(testQueue.testMode.jobs[0].data).to.eql({
	    phoneNumber: '+24153518780',
	    message: 'This is the code 1234 to verify your account',
	});

	expect(testQueue.testMode.jobs[1].type).to.equal('push_notification_code_3');

	expect(queue.testMode.jobs[1].data).to.eql({
	    phoneNumber: '+25153118782',
	    message: 'This is the code 38998 to verify your account',
	});
    });
});