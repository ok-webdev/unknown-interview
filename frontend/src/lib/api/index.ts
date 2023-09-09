import createClient from 'openapi-fetch';
import type { paths } from '$lib/openapi'; // generated from openapi-typescript
import { browser } from '$app/environment';

const api = createClient<paths>({
	baseUrl: browser
		? undefined
		: process.env.STAGE === 'dev'
		? 'http://dev-backend:8000'
		: process.env.isDocker
		? 'http://client:80'
		: 'http://localhost:2080'
});
export default api;
