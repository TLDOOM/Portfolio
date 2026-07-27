// src/routes/projects/+page.ts
import { PUBLIC_API_URL} from '$env/static/public';
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    const res = await fetch(`${PUBLIC_API_URL}/projects`);
    const projects = await res.json();

    const res2 = await fetch(`${PUBLIC_API_URL}/future`);
    const future =await res2.json();

    return {
        projects,
        future
    };
};
 