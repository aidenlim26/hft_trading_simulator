================================================================================
PROJECT: ALGORITHMIC HIGH-FREQUENCY TRADING (HFT) SIMULATOR
================================================================================
Objective:
    Build an in-memory financial market matching engine that simulates an order 
    book for high-frequency trading. The system ingests dynamic order streams, 
    maintains a strictly sorted multi-dimensional order book, matches buyers 
    and sellers based on price priority, and updates portfolio states in real-time.

Author: Lim Lok Chun Aiden
Date: June 2026
Language: Python 3.x (Standard Library Only)
================================================================================

--------------------------------------------------------------------------------
1. OBJECT-ORIENTED PROGRAMMING (OOP) ARCHITECTURE
--------------------------------------------------------------------------------
* Modular Design: Separated into clean domain modules (models, engine, utilities)
  to ensure tight encapsulation and single-responsibility boundaries.
* Domain Modeling: 
    - `Order`: Encapsulates immutability of transaction metrics via constructors.
    - `OrderBook`: Coordinates stateful, bidirectional trade liquidity.
    - `Trader`: Manages private ledger records, validation balances, and portfolios.
* Exception Handling: Implements custom try-except frameworks to catch, log,
  and gracefully skip corrupted or malformed network/file data streams.

--------------------------------------------------------------------------------
2. DATA STRUCTURES & MEMORY MANAGEMENT
--------------------------------------------------------------------------------
* Hash Maps (Dictionaries): Utilized for O(1) tracking of trader portfolios 
  and quick indexing of active stock symbols.
* Linear Arrays (Lists): Used to store collections of live order objects 
  representing current bids and asks.
* Tuples: Deployed for immutable, light-weight snapshots of market data, 
  such as the instantaneous Bid-Ask spread.
* Unpacking Mechanics: Uses Python unpacking (*args, **kwargs) to cleanly 
  instantiate dynamic configurations and order payloads.

--------------------------------------------------------------------------------
3. DATA STRUCTURES & ALGORITHMS (DSA) APPLICATION
--------------------------------------------------------------------------------
* Sorting Implementations:
    - Custom Quick Sort: Used to sort incoming batch transactions based on 
      object attribute priorities (order.price).
    - Recursive Binary Insertion: Combines recursive state reduction with 
      binary search patterns to find the exact insertion point for an unmatched 
      order, maintaining a strictly sorted book at O(log N) search speed.
* Searching Algorithms: Leverages fast search logic to handle instant user/bot 
  order cancelations within the array blocks.
* String Manipulation: Heavy parsing, stripping, and sanitizing of raw 
  historical CSV/TXT ticker feeds, followed by explicit type conversion 
  safeguards before object instantiation.
* Stream formatting: Leverages advanced string padding and numeric precision 
  formatting to yield clean, scannable terminal terminal dashboards.

================================================================================