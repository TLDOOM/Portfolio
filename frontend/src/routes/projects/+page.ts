// src/routes/projects/+page.ts
import type { PageLoad } from './$types';

export const load: PageLoad = async ({ fetch }) => {
    const res = await fetch('http://localhost:8000/projects');
    const projects = await res.json();

    const res2 = await fetch('http://localhost:8000/future');
    const future =await res2.json();

    return {
        projects,
        future
    };
};
 