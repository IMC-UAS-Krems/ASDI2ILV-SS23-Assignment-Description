# ASDI2ILV SS23 Assignment Description

## Repo Structure
This repository has the following structure:

```
.
├── README.md
├── __init__.py
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_sample.py
```

> **NOTE** the content of this repository may change as the result of in-class discussion or the definition of new public test cases (new files inside the `tests` folder). Make sure you always check out the latest version of this repository from GitHub!

## Task Description

You are developing a new social media platform on which friends communicate by posting messages.

A user can `send` a direct message to another user only if they are connected as friends. Users can also `post` a group message to all her/his friends. When a user `post` a group message, the message must be automatically delivered to all her/his direct friends and, transitively, to the friends of their friends.

A message contains:

- the unique and lowercase name of the sender
- the unique and lowercase name of the recipient or `None` (`None` indicates a group message)
- the timestamp indicating when the message was sent or posted. Timestamp is formed by a date `DD/MM/YYYY` and a time `hh:mm:ss`
- the message body consisting only by lowercase characters [a-z] and spaces [ ]. An empty body is allowed.

An example of a message posted the 1st September 2022 at 09:00:00 AM from `adam` to all the friends might look like:

```
sender: adam
timestamp: 01/09/2022 09:00:00
recipient: None
body: grill at my place
``` 

The platform should not lose or inject any message, and messages should be `read` sorted either by `timestamp` or `sender`.

Additionally, since the platform owners want to minimize the costs of transmitting those messages, the platform must compress the message bodies before delivering the messages to the recipient(s).

Compression works by translating **each word** into a sequence of bytes, and compress each word using Huffman string encoding (the Huffman table is give [here](HUFFMAN_TABLE.md).

For example, given the message:
```
grill at my place
```

The message encoded using Huffman should be:

```
00010010010111111111111 1110001 110011111100 010111111111110111101100
```
> **Note**: words are kept separated!

Before a recipient can read messages, the platform must decode their body.

Decoding requires to match the codes from the [Huffman table](HUFFMAN_TABLE.md).

> **Note** In the Huffman table, codes are defined such that they share not prefix, so it is always possible to identify them in the stream of bits.