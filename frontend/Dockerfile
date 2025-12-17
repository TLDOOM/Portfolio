# Use official Node.js image
FROM node:20

# Set working directory
WORKDIR /app

# Copy only package files first (for caching)
COPY package*.json ./

# Clean install to avoid Rollup optional dependency errors
RUN rm -rf node_modules package-lock.json \
    && npm install

# Copy the rest of the source code
COPY . .

# Expose SvelteKit dev server port
EXPOSE 5173

# Start SvelteKit dev server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "5173"]
