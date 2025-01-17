import { skeleton } from '@skeletonlabs/tw-plugin';
import { join } from 'path';
import type { Config } from 'tailwindcss';
import plugin from 'tailwindcss/plugin';
import defaultTheme from 'tailwindcss/defaultTheme';

export default {
	content: [
		'./src/**/*.{html,js,svelte,ts}',
		join(require.resolve('@skeletonlabs/skeleton'), '../**/*.{html,js,svelte,ts}')
	],
	theme: {
		extend: {
			fontFamily: {
				title: ['Comfortaa', ...defaultTheme.fontFamily.sans],
				body: ['Montserrat', ...defaultTheme.fontFamily.sans]
			},
			colors: {
				app: {
					blue: {
						50: '#EAF4FD',
						100: '#CBE6F7',
						400: '#4DA9E9',
						500: '#2B93E1',
						600: '#1985E2'
					}
				}
			}
		}
	},
	plugins: [
		plugin(({ addVariant }) => {
			addVariant('current', ['&:focus-within', '&:hover']);
			addVariant('group-current', [':merge(.group):focus-within &', ':merge(.group):hover &']);
			addVariant('peer-current', [':merge(.peer):focus-within ~ &', ':merge(.peer):hover ~ &']);
		}),
		skeleton
	]
} satisfies Config;
