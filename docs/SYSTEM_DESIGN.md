# System Design Interview Guide

> **Essential for Senior/Staff Engineer roles at FAANG and top tech companies**

## Table of Contents
1. [Fundamentals](#fundamentals)
2. [Framework for System Design Interviews](#framework)
3. [Common Problems with Solutions](#common-problems)
4. [Key Concepts](#key-concepts)
5. [Estimation Techniques](#estimation)
6. [Resources](#resources)

---

## Fundamentals

### Core Principles

#### 1. **Scalability**
- **Vertical Scaling (Scale Up)**: Add more power (CPU, RAM) to existing machines
  - Pros: Simple, no code changes
  - Cons: Hardware limits, single point of failure, expensive

- **Horizontal Scaling (Scale Out)**: Add more machines
  - Pros: Linear scaling, fault tolerant, cost effective
  - Cons: Complex, need load balancing, data consistency challenges

#### 2. **Load Balancing**
Distribute traffic across multiple servers

**Algorithms**:
- Round Robin: Distribute requests sequentially
- Least Connections: Send to server with fewest active connections
- IP Hash: Route based on client IP
- Least Response Time: Send to fastest responding server

**Types**:
- Layer 4 (Transport): Based on IP/Port
- Layer 7 (Application): Based on HTTP headers, URL, cookies

#### 3. **Caching**
Store frequently accessed data in fast storage

**Strategies**:
- **Write-Through**: Write to cache and DB simultaneously
  - Pros: Data consistency
  - Cons: Higher write latency

- **Write-Back (Write-Behind)**: Write to cache, async write to DB
  - Pros: Low write latency
  - Cons: Risk of data loss

- **Write-Around**: Write to DB, bypass cache
  - Pros: Avoid cache pollution
  - Cons: Cache miss on recent writes

**Eviction Policies**: LRU, LFU, FIFO, Random

**Levels**:
- Client-side (Browser)
- CDN (Static content)
- Application cache (Redis, Memcached)
- Database cache

#### 4. **Database Concepts**

**SQL vs NoSQL**:

| Aspect | SQL | NoSQL |
|--------|-----|-------|
| Schema | Fixed schema | Flexible schema |
| Scalability | Vertical (mostly) | Horizontal |
| ACID | Yes | Eventually consistent |
| Use Case | Complex queries, transactions | High throughput, simple queries |
| Examples | PostgreSQL, MySQL | MongoDB, Cassandra, DynamoDB |

**Database Sharding**:
- Split data across multiple databases
- Strategies:
  - **Horizontal**: Split rows (by user ID range)
  - **Vertical**: Split columns (different tables)
  - **Hash-based**: Hash key determines shard
  - **Geographic**: By region/location

**Replication**:
- **Master-Slave**: One write master, multiple read replicas
- **Master-Master**: Multiple write masters (conflict resolution needed)
- **Benefits**: Reliability, read scalability, geographic distribution

**Indexing**:
- B-Tree indexes for range queries
- Hash indexes for equality lookups
- Trade-off: Faster reads, slower writes, more storage

#### 5. **CAP Theorem**
You can only guarantee 2 out of 3:
- **C**onsistency: All nodes see same data
- **A**vailability: Every request gets response
- **P**artition Tolerance: System works despite network failures

**In Practice**:
- CA: Traditional RDBMS (not partition tolerant)
- CP: MongoDB, HBase (sacrifice availability)
- AP: Cassandra, DynamoDB (eventual consistency)

#### 6. **Message Queues**
Asynchronous communication between services

**Benefits**:
- Decouple services
- Handle traffic spikes
- Retry failed operations
- Order processing

**Examples**: RabbitMQ, Apache Kafka, AWS SQS

#### 7. **Microservices**
Break monolith into small, independent services

**Pros**:
- Independent deployment
- Technology flexibility
- Team autonomy
- Fault isolation

**Cons**:
- Distributed system complexity
- Network latency
- Data consistency challenges
- Operational overhead

---

## Framework for System Design Interviews

### Step-by-Step Approach (45-60 minutes)

#### **Step 1: Clarify Requirements (3-5 min)**
**Functional**:
- Core features needed?
- Who are the users?
- How will they use it?

**Non-Functional**:
- Scale: DAU (Daily Active Users), TPS (Transactions/sec)?
- Performance: Latency requirements?
- Availability: 99.9%? 99.99%?
- Consistency: Strong or eventual?

**Example Questions**:
- "Should we support mobile and web?"
- "Is this read-heavy or write-heavy?"
- "What's the expected growth over next 5 years?"

#### **Step 2: Estimation (5 min)**
**Calculate**:
- Storage needed (5 years)
- Bandwidth (read/write QPS)
- Memory for cache (80-20 rule)

**Example**:
```
100M DAU
Each user posts 2 tweets/day = 200M writes/day
200M / 86400 = ~2,300 writes/sec
Each tweet = 140 chars + metadata = 300 bytes
Daily storage = 200M * 300B = 60GB/day
5 year storage = 60GB * 365 * 5 = ~110TB
```

#### **Step 3: High-Level Design (10-15 min)**
**Draw Components**:
- Client (Web/Mobile)
- Load Balancer
- API Servers
- Database(s)
- Cache
- CDN
- Message Queue

**Define API**:
```
POST /api/v1/posts
GET /api/v1/posts/{post_id}
GET /api/v1/feed?user_id={id}
DELETE /api/v1/posts/{post_id}
```

#### **Step 4: Deep Dive (15-20 min)**
**Interviewer will guide you**. Common topics:
- Database schema design
- Scaling specific components
- Handling failures
- Caching strategy
- Consistency vs Availability tradeoffs

#### **Step 5: Bottlenecks & Refinement (5-10 min)**
- Identify single points of failure
- Address scaling concerns
- Discuss monitoring and alerts
- Trade-offs made

---

## Common Problems with Solutions

### 1. **URL Shortener (e.g., TinyURL, bit.ly)**

**Difficulty**: Entry-Level | **Time**: 45 min | **Companies**: All FAANG

#### Requirements
- Shorten long URL to short URL
- Redirect short URL to original
- 100M URLs/month, 100:1 read:write ratio

#### Scale Estimation
```
Write: 100M/month ≈ 40 writes/sec
Read: 40 * 100 = 4,000 reads/sec
Storage: 100M URLs * 12 months * 5 years * 500 bytes = 300GB
```

#### High-Level Design
```
[Client]
   ↓
[Load Balancer]
   ↓
[API Servers] ←→ [Cache (Redis)] ←→ [Database (NoSQL)]
                                         ↓
                                    [Cleanup Service]
```

#### Key Points
- **URL Generation**:
  - Hash (MD5/SHA): Collision handling needed
  - Base62 encoding of auto-increment ID: 7 chars = 62^7 = 3.5 trillion URLs

- **Database Schema**:
```sql
ShortURL Table:
- short_url (PK): varchar(7)
- long_url: varchar(2048)
- created_at: timestamp
- expires_at: timestamp
- user_id: bigint
Index on: short_url, user_id
```

- **API**:
```
POST /shorten
Body: { "long_url": "..." }
Response: { "short_url": "abc1234" }

GET /{short_url}
Response: HTTP 302 redirect
```

- **Scaling**:
  - Cache popular URLs (80-20 rule)
  - Database sharding by hash(short_url)
  - CDN for static redirect page
  - Rate limiting per user

---

### 2. **Design Twitter / News Feed**

**Difficulty**: Medium | **Time**: 60 min | **Companies**: Meta, Twitter, LinkedIn

#### Requirements
- Post tweets (280 chars)
- Follow users
- View timeline (feed)
- 200M DAU, 50M active posters

#### Scale Estimation
```
Tweets: 50M users * 2 tweets/day = 100M tweets/day ≈ 1,200 writes/sec
Reads: 200M users * 20 feed refreshes/day = 4B reads/day ≈ 46K reads/sec
Storage: 100M * 300 bytes * 365 * 5 = 55TB
```

#### High-Level Design
```
[Client]
   ↓
[API Gateway/Load Balancer]
   ↓         ↓              ↓
[Write API] [Read API]  [Media Service]
   ↓           ↓              ↓
[Tweet DB]  [Feed Cache]  [Object Storage (S3)]
   ↓           ↑
[Fanout Service]
```

#### Key Components

**1. Write Path (Post Tweet)**:
```
User posts → Write API → Store in Tweet DB
                       → Fanout Service → Push to followers' feeds (cache)
```

**2. Read Path (View Feed)**:
```
User requests feed → Read API → Check Feed Cache → Return cached feed
                                  ↓ (if miss)
                                Aggregate from User Graph + Tweet DB
```

#### Database Schema
```sql
Users: user_id, username, email, created_at
Tweets: tweet_id, user_id, content, created_at, likes, retweets
Followers: user_id, follower_id, created_at
Timeline: user_id, tweet_id, timestamp (cached feed)
```

#### Fanout Strategies

**Fanout on Write** (Push):
- Pre-compute feed when tweet is posted
- Fast reads
- Slow writes for celebrities (millions of followers)

**Fanout on Read** (Pull):
- Compute feed when requested
- Slow reads
- Fast writes

**Hybrid** (Best):
- Push for most users
- Pull for celebrities
- Hybrid for power users

#### Optimizations
- Cache user timelines in Redis (LRU eviction)
- Shard tweets by tweet_id (Consistent Hashing)
- Separate hot/cold storage (recent tweets in memory)
- CDN for media files
- Message queue for async fanout

---

### 3. **Design Instagram**

**Difficulty**: Medium | **Time**: 60 min | **Companies**: Meta, Pinterest, Snap

#### Unique Challenges vs Twitter
- Heavy image/video storage
- Image processing pipeline
- Feed algorithm (ML-based ranking)

#### Additional Components
```
[Upload Service]
   ↓
[Image Processing Service] → Multiple sizes/formats
   ↓
[Object Storage (S3/GCS)]
   ↓
[CDN] → Serve images globally
```

#### Image Storage
- Original image: S3/GCS
- Processed versions: Multiple sizes (thumbnail, medium, full)
- CDN: CloudFront, Cloudflare
- Metadata: Database (image_id, user_id, location, tags)

#### Feed Ranking
- Simple: Chronological
- Advanced: ML model considering:
  - User engagement history
  - Post recency
  - Relationship strength
  - Content type preferences

---

### 4. **Design Rate Limiter**

**Difficulty**: Entry-Medium | **Time**: 45 min | **Companies**: All

#### Requirements
- Limit requests per user/IP
- Configurable rules (e.g., 100 req/min)
- Distributed system
- Low latency (<1ms overhead)

#### Algorithms

**1. Token Bucket** ⭐ Most Popular
```
- Bucket has max tokens
- Tokens refill at constant rate
- Each request consumes 1 token
- Reject if no tokens

Pros: Smooth traffic, handles bursts
Cons: Memory per user
```

**2. Leaky Bucket**
```
- Requests enter queue
- Process at fixed rate
- Drop if queue full

Pros: Constant output rate
Cons: Old requests may wait long
```

**3. Fixed Window Counter**
```
- Count requests in fixed time window
- Reset counter each window

Pros: Simple, memory efficient
Cons: Burst at window edges
```

**4. Sliding Window Log**
```
- Store timestamp of each request
- Count requests in last N seconds

Pros: Accurate
Cons: Memory intensive
```

#### Implementation (Token Bucket in Redis)
```python
# Redis key: rate_limit:{user_id}
# Value: { tokens: int, last_refill: timestamp }

def allow_request(user_id, max_tokens=100, refill_rate=1):
    key = f"rate_limit:{user_id}"
    data = redis.get(key)

    now = time.now()
    if not data:
        data = {'tokens': max_tokens - 1, 'last_refill': now}
        redis.set(key, data, ex=60)
        return True

    # Refill tokens
    elapsed = now - data['last_refill']
    tokens_to_add = elapsed * refill_rate
    current_tokens = min(max_tokens, data['tokens'] + tokens_to_add)

    if current_tokens >= 1:
        data['tokens'] = current_tokens - 1
        data['last_refill'] = now
        redis.set(key, data, ex=60)
        return True
    return False
```

#### Distributed Rate Limiting
- **Centralized**: Redis cluster (single source of truth)
- **Sticky Sessions**: Route same user to same server
- **Eventually Consistent**: Each server tracks independently, over-limit ok briefly

---

### 5. **Design Web Crawler**

**Difficulty**: Medium | **Time**: 60 min | **Companies**: Google, Amazon

#### Requirements
- Crawl 1 billion pages/month
- Extract and store content
- Respect robots.txt
- Avoid traps (infinite links)

#### Components
```
[Seed URLs]
     ↓
[URL Frontier (Queue)]
     ↓
[HTML Downloader]
     ↓
[Content Parser] → [Duplicate Detector (Bloom Filter)]
     ↓                    ↓
[URL Extractor]      [Storage (S3/DB)]
     ↓
[URL Filter] → Back to Frontier
```

#### Key Challenges

**1. Politeness**
- Respect robots.txt
- Rate limit per domain (1 request/sec)
- Use priority queue

**2. Duplicate Detection**
- URL normalization
- Content hash (MD5)
- Bloom filter for memory efficiency

**3. Scalability**
- Distribute crawlers geographically
- Partition URL frontier by domain
- Horizontal scaling of all components

**4. Robustness**
- Handle failures (retry with backoff)
- Detect crawler traps (URL depth limit)
- Handle various content types

#### URL Frontier Design
```
Priority Queue:
- High: .gov, .edu, popular sites
- Medium: .com, .org
- Low: others

Per-domain Queue:
- Ensure politeness
- Avoid overwhelming single site
```

---

### 6. **Design YouTube / Video Streaming**

**Difficulty**: Hard | **Time**: 60 min | **Companies**: Google, Netflix, Amazon

#### Scale
- 2 billion users
- 500 hours of video uploaded/minute
- 1 billion hours watched/day

#### Architecture
```
[Upload Flow]
User → Upload Service → Object Storage (S3)
                       → Transcoding Service → Multiple formats (360p, 720p, 1080p, 4K)
                       → Thumbnail Generation
                       → Metadata DB

[Streaming Flow]
User → API → CDN → Adaptive Bitrate Streaming
```

#### Key Components

**1. Video Upload**
- Resumable upload (handle interruptions)
- Chunk-based upload
- Pre-signed URLs (direct to S3)

**2. Video Processing**
- Transcoding to multiple resolutions
- Generate thumbnails at key frames
- Extract audio track
- Generate subtitles (ML)
- Distributed processing (Map-Reduce)

**3. Video Storage**
- Original: S3 (cold storage)
- Processed: S3 + CDN
- Popular videos: Hot cache
- Metadata: SQL/NoSQL database

**4. Streaming**
- **DASH/HLS**: Adaptive bitrate
- **CDN**: 95%+ traffic served from edge
- **Protocol**: HTTP/2, QUIC

#### Database Schema
```sql
Videos: video_id, user_id, title, description, upload_date, view_count
Users: user_id, username, email, subscribers
Comments: comment_id, video_id, user_id, text, timestamp
Likes: video_id, user_id, timestamp
```

#### Recommendations
- Collaborative filtering
- Content-based filtering
- ML model on user history
- Real-time vs batch processing

---

### 7. **Design Uber / Ride-Sharing**

**Difficulty**: Hard | **Time**: 60 min | **Companies**: Uber, Lyft, DoorDash

#### Requirements
- Match riders with drivers
- Real-time location tracking
- Pricing (surge pricing)
- Payment processing
- 100M rides/day

#### Architecture
```
[Mobile App (Rider/Driver)]
        ↓         ↓
   [WebSocket] [REST API]
        ↓         ↓
   [Location Service] ← [Geospatial Index (QuadTree/S2)]
        ↓
   [Matching Service]
        ↓
   [Trip Service] → [Database]
        ↓
   [Payment Service]
```

#### Key Challenges

**1. Geospatial Indexing**
- **QuadTree**: Divide map into grids
- **Geohash**: Encode lat/long to string
- **S2 Geometry**: Google's library (used by Uber)

**2. Matching Algorithm**
- Find nearest available drivers (within 5-10 km)
- Priority: Distance, driver rating, ETA
- Broadcast to top 5 drivers
- First to accept gets ride

**3. Real-time Location**
- Drivers send location every 4 seconds
- Use WebSockets for bidirectional communication
- Store in Redis (key: driver_id, value: {lat, lon, timestamp})
- Update geospatial index

**4. Surge Pricing**
- Supply/Demand algorithm
- Geohash-based regions
- Real-time computation
- Notify users before confirming

**5. Trip State Machine**
```
Requested → Accepted → Arrived → Started → Completed → Paid
```

#### Database Schema
```sql
Drivers: driver_id, name, phone, rating, status, current_lat, current_lon
Riders: rider_id, name, phone, rating
Trips: trip_id, rider_id, driver_id, status, pickup_loc, dropoff_loc, fare, created_at
Locations: trip_id, lat, lon, timestamp (GPS trail)
```

#### Optimizations
- Cache frequent locations
- Precompute ETAs for popular routes
- Batch location updates
- Use message queue for async notifications

---

### 8. **Design Distributed Cache (like Redis)**

**Difficulty**: Medium-Hard | **Time**: 60 min | **Companies**: All

#### Requirements
- Key-value store
- High performance (< 1ms latency)
- Distributed across nodes
- Fault tolerant

#### Architecture
```
[Client]
    ↓
[Client Library] → Hash(key) → Determine Node
    ↓
[Cache Nodes] → Master-Slave replication
    ↓
[Persistence Layer]
```

#### Key Concepts

**1. Consistent Hashing**
- Minimize data movement when nodes added/removed
- Virtual nodes for even distribution

**2. Replication**
- Master-Slave for each shard
- Async replication for performance
- Leader election (Raft/Paxos)

**3. Eviction Policies**
- LRU (Least Recently Used)
- LFU (Least Frequently Used)
- TTL (Time To Live)

**4. Data Structures**
- Strings, Lists, Sets, Sorted Sets, Hashes
- In-memory with optional persistence

**5. Persistence**
- **RDB**: Snapshot at intervals
- **AOF**: Append-only file (every write)
- Hybrid approach

#### Handling Failures
- Health checks (heartbeat)
- Replica promotion
- Gossip protocol for cluster state
- Client-side caching for resilience

---

### 9. **Design Search Autocomplete / Typeahead**

**Difficulty**: Medium | **Time**: 45 min | **Companies**: Google, Amazon

#### Requirements
- Suggest top 5 queries as user types
- Handle 10M DAU
- Low latency (< 100ms)

#### Data Collection
```
User searches → Log search queries → Aggregate counts
                                   → Build suggestion database
```

#### Storage Options

**1. Trie (Prefix Tree)** ⭐
- Fast prefix lookup O(length of prefix)
- Store top N suggestions at each node
- Memory intensive for large datasets

**2. Database with Prefix Index**
- Table: (query, frequency, last_updated)
- Index on query prefix
- Slower than Trie but more flexible

#### Architecture
```
[Client]
    ↓
[API Gateway]
    ↓
[Autocomplete Service] → [Trie Cache (Redis)]
                       → [Database (backup)]
    ↑
[Data Aggregation Service] → Update Trie periodically
```

#### Optimization
- Cache top 1000 queries
- Personalization (user history)
- Trending queries (real-time updates)
- Geographic relevance

#### Data Updates
- Real-time: Complex, expensive
- Batch: Update Trie every hour
- Hybrid: Real-time for trending, batch for long-tail

---

### 10. **Design Notification System**

**Difficulty**: Medium | **Time**: 45 min | **Companies**: All

#### Requirements
- Send notifications (push, email, SMS)
- 100M notifications/day
- Delivery guarantees
- Prevent spam

#### Architecture
```
[Services] → [Notification Service] → [Message Queue]
                                         ↓
                            [Workers] → [Push/Email/SMS Providers]
                                         ↓
                                    [User Devices]
```

#### Components

**1. Notification Service**
- Receive notification requests
- Validate and enrich data
- Determine delivery channel
- Rate limiting (prevent spam)

**2. Message Queue**
- Decouple producers/consumers
- Handle traffic spikes
- Retry failed notifications
- Priority queue (urgent vs normal)

**3. Workers**
- Poll queue
- Call third-party APIs (FCM, SendGrid, Twilio)
- Track delivery status
- Handle failures

**4. User Preferences**
- Opt-in/opt-out
- Channel preferences (email vs push)
- Quiet hours
- Notification grouping

#### Database Schema
```sql
Notifications: notification_id, user_id, type, channel, content, status, created_at
UserPreferences: user_id, channel, enabled, quiet_start, quiet_end
Templates: template_id, type, subject, body, variables
DeliveryLog: notification_id, status, attempts, delivered_at
```

#### Reliability
- At-least-once delivery (retry with idempotency)
- Dead letter queue for failed notifications
- Exponential backoff for retries
- Monitor delivery rates

#### Optimizations
- Batch notifications (digest emails)
- Template caching
- Geographic routing (send from nearest region)
- Prioritize important notifications

---

## Key Concepts Deep Dive

### API Design

**RESTful Principles**:
```
GET    /users/{id}         - Fetch user
POST   /users              - Create user
PUT    /users/{id}         - Update user
DELETE /users/{id}         - Delete user

GET    /users/{id}/posts   - Fetch user's posts
POST   /users/{id}/posts   - Create post for user
```

**Versioning**:
- URL: `/api/v1/users`
- Header: `Accept: application/vnd.api.v1+json`

**Pagination**:
```
GET /posts?page=1&limit=20
Response: { data: [...], next_page: 2, total: 1000 }
```

### Monitoring & Observability

**Metrics to Track**:
- Latency (p50, p95, p99)
- Throughput (QPS)
- Error rate
- CPU/Memory usage
- Database connections

**Tools**:
- Prometheus + Grafana
- DataDog
- New Relic
- CloudWatch (AWS)

**Logging**:
- Structured logs (JSON)
- Correlation IDs for distributed tracing
- Log aggregation (ELK stack)

**Alerting**:
- PagerDuty, Opsgenie
- Alert on trends, not just thresholds
- Runbooks for common issues

---

## Estimation Techniques

### Power of 2 Table
```
2^10 = 1,024 ≈ 1 Thousand (1 KB)
2^20 = 1,048,576 ≈ 1 Million (1 MB)
2^30 = 1,073,741,824 ≈ 1 Billion (1 GB)
2^40 ≈ 1 Trillion (1 TB)
```

### Latency Numbers
```
L1 cache reference: 0.5 ns
L2 cache reference: 7 ns
Main memory reference: 100 ns
SSD random read: 150 μs
HDD seek: 10 ms
Network round trip (same datacenter): 0.5 ms
Network round trip (cross-continent): 150 ms
```

### Availability Numbers
```
99% = 3.65 days downtime/year
99.9% (3 nines) = 8.76 hours/year
99.99% (4 nines) = 52.6 minutes/year
99.999% (5 nines) = 5.26 minutes/year
```

### Back-of-Envelope Calculations
```
1M users * 100 requests/day = 100M requests/day
100M / 86,400 seconds ≈ 1,200 QPS (average)
Peak QPS = 2-3x average = 3,600 QPS

Storage: 1M users * 1KB/user = 1GB
5 years = 1GB * 365 * 5 = 1.8TB
```

---

## Resources

### Books
- "Designing Data-Intensive Applications" by Martin Kleppmann ⭐
- "System Design Interview" by Alex Xu (Vol 1 & 2) ⭐
- "Building Microservices" by Sam Newman

### Online Resources
- [System Design Primer](https://github.com/donnemartin/system-design-primer) (GitHub)
- [Grokking the System Design Interview](https://www.educative.io/courses/grokking-the-system-design-interview)
- [ByteByteGo Newsletter](https://blog.bytebytego.com/)

### Practice Platforms
- Pramp (mock interviews)
- Exponent (system design courses)
- LeetCode Discuss (real interview questions)

### Real-World Architectures
- [High Scalability Blog](http://highscalability.com/)
- Engineering blogs: Netflix, Uber, Airbnb, LinkedIn

---

## Interview Tips

### Do's ✅
- Ask clarifying questions
- Start with high-level design
- Discuss trade-offs
- Consider failure scenarios
- Estimate numbers
- Draw diagrams
- Think out loud
- Be open to feedback

### Don'ts ❌
- Jump into details too quickly
- Design overly complex systems
- Ignore constraints
- Assume infinite resources
- Forget about edge cases
- Ignore interviewer hints
- Be defensive about choices
- Forget to summarize

### Common Mistakes
1. **Over-engineering**: Keep it simple initially
2. **Under-estimating scale**: Always ask about numbers
3. **Ignoring bottlenecks**: Identify and address them
4. **Poor communication**: Explain your thought process
5. **Not considering failures**: Discuss fault tolerance

---

## Practice Problems

For practice, try designing:
1. Design Slack / WhatsApp (messaging)
2. Design Spotify (music streaming)
3. Design Google Drive (file storage)
4. Design Amazon (e-commerce)
5. Design Ticketmaster (ticket booking)
6. Design Facebook Messenger
7. Design Netflix Recommendation System
8. Design GitHub (version control)
9. Design Dropbox
10. Design Yelp (location-based search)

**Time yourself**: 45-60 minutes per design

---

Remember: **There's no single correct answer**. Focus on demonstrating your thought process, considering trade-offs, and designing systems that meet requirements at scale.

Good luck! 🚀
