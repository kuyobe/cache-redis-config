# cache-redis-config
======================

### Description
---------------

cache-redis-config is a lightweight, flexible, and highly scalable Redis configuration manager for caching data in your application. It allows you to easily switch between different Redis configurations, manage caching policies, and monitor performance metrics.

### Features
-------------

* **Configurable caching policies**: Easily switch between different caching policies, such as LRU, LFU, and TTL.
* **Redis configuration management**: Manage Redis connections, including host, port, and password.
* **Performance metrics**: Monitor and track Redis performance metrics, including cache hits, misses, and evictions.
* **Cache statistics**: View detailed cache statistics, such as cache size, hit ratio, and evictions.
* **Easy integration**: Simple and straightforward API for easy integration with your application.

### Technologies Used
-------------------

* **Redis**: The popular in-memory data store.
* **Node.js**: The JavaScript runtime environment for building scalable and high-performance applications.
* **Express**: The popular Node.js web framework for building web applications.

### Installation
-------------

To install cache-redis-config, run the following command in your terminal:

```bash
npm install cache-redis-config
```

### Usage
-----

### Getting Started
-----------------

To use cache-redis-config, create a new instance of the RedisConfig class, and specify the Redis connection details:

```javascript
const RedisConfig = require('cache-redis-config');

const redisConfig = new RedisConfig({
  host: 'localhost',
  port: 6379,
  password: 'your_password'
});
```

### Caching Policies
-----------------

You can switch between different caching policies using the `policy` property:

```javascript
redisConfig.policy = 'lru'; // Set the caching policy to LRU
```

### Performance Metrics
---------------------

You can enable performance metrics by setting the `metrics` property:

```javascript
redisConfig.metrics = true; // Enable performance metrics
```

### Cache Statistics
------------------

You can view detailed cache statistics using the `stats` property:

```javascript
const stats = redisConfig.stats; // Get cache statistics
console.log(stats); // Output: { hits: 100, misses: 20, evictions: 10 }
```

### API
-----

### Methods
---------

* `connect()`: Establishes a connection to Redis.
* `disconnect()`: Disconnects from Redis.
* `get(key)`: Retrieves a value from the cache.
* `set(key, value)`: Sets a value in the cache.
* `expire(key, ttl)`: Sets a TTL for a key.
* `del(key)`: Deletes a key from the cache.

### License
--------

cache-redis-config is licensed under the MIT License.

### Contributing
--------------

Contributions are welcome! Please submit pull requests or issues to the project repository.