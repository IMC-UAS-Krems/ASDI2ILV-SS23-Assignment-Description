from solution.platform import Person, Message, SocialNetwork, SortCriteria


def test_send_direct_message_to_friend():
    """
    Test that a message directly sent from a friend to another is correctly delivered
    :return:
    """
    sn = SocialNetwork()

    adam = Person("adam")
    sn.register(adam)

    bob = Person("bob")
    sn.register(bob)

    sn.declare_friendship(adam, bob)

    greetings = "hi bob nice to see you"
    a_message_from_adam_to_bob = Message(adam, bob, greetings )

    sn.send(a_message_from_adam_to_bob)

    # Adam did not receive his message
    assert len(adam.read_messages(SortCriteria.SENDER)) == 0

    messages_to_bob = bob.read_messages(SortCriteria.SENDER)
    # Bob received one message
    assert len(messages_to_bob) == 1
    # The message Bob received is the one sent by Adam
    assert messages_to_bob[0].body == greetings
    assert messages_to_bob[0].sender == adam


def test_send_group_message_to_friend():
    """
    Test that a message sent to the group of friend is correctly delivered. This test cover the case in which only one
    friend is there
    :return:
    """
    sn = SocialNetwork()

    adam = Person("adam")
    sn.register(adam)

    bob = Person("bob")
    sn.register(bob)

    sn.declare_friendship(adam, bob)

    greetings = "grill at my place"
    a_message_from_adam_to_all_friends = Message(adam, None, greetings )

    sn.send(a_message_from_adam_to_all_friends)

    # Adam did not receive his message
    assert len(adam.read_messages(SortCriteria.SENDER)) == 0

    messages_to_bob = bob.read_messages(SortCriteria.SENDER)
    # Bob received one message
    assert len(messages_to_bob) == 1
    # The message Bob received is the one sent by Adam
    assert messages_to_bob[0].body == greetings
    assert messages_to_bob[0].sender == adam


def test_send_group_message_reaches_all_friends():
    """
    Test that a message directly sent from a friend to another is correctly delivered
    :return:
    """
    sn = SocialNetwork()

    adam = Person("adam")
    sn.register(adam)

    bob = Person("bob")
    sn.register(bob)

    # Adam and Bob are friends
    sn.declare_friendship(adam, bob)

    carol = Person("carol")
    sn.register(carol)

    # Bob and Carol are also friends
    sn.declare_friendship(bob, carol)

    greetings = "grill at my place"
    a_message_from_adam_to_all_friends = Message(adam, None, greetings )

    sn.send(a_message_from_adam_to_all_friends)

    # Adam did not receive his message
    assert len(adam.read_messages(SortCriteria.SENDER)) == 0

    messages_to_bob = bob.read_messages(SortCriteria.SENDER)
    # Bob received one message
    assert len(messages_to_bob) == 1
    # The message Bob received is the one sent by Adam
    assert messages_to_bob[0].body == greetings
    assert messages_to_bob[0].sender == adam

    messages_to_carol = carol.read_messages(SortCriteria.SENDER)
    # Carol also received one message, since she's friend with Bob
    assert len(messages_to_carol) == 1
    # The message Bob received is the one sent by Adam
    assert messages_to_carol[0].body == greetings
    assert messages_to_carol[0].sender == adam


def test_friendships_survive():
    """
    If two persons A and C become friends via another person B that leaves the platform. A and C remains friends.
    :return:
    """
    sn = SocialNetwork()

    adam = Person("adam")
    sn.register(adam)

    bob = Person("bob")
    sn.register(bob)

    # Adam and Bob are friends
    sn.declare_friendship(adam, bob)

    carol = Person("carol")
    sn.register(carol)

    # Bob and Carol are also friends
    sn.declare_friendship(bob, carol)

    # At this point Bob leaves the platform
    sn.deregister(bob)

    # Messages sent by Adam are received by Carol
    greetings = "grill at my place"
    a_message_from_adam_to_all_friends = Message(adam, None, greetings )

    sn.send(a_message_from_adam_to_all_friends)

    # Adam did not receive his message
    assert len(adam.read_messages(SortCriteria.SENDER)) == 0

    messages_to_carol = carol.read_messages(SortCriteria.SENDER)
    # Carol also received one message, since she's friend with Bob
    assert len(messages_to_carol) == 1
    # The message Bob received is the one sent by Adam
    assert messages_to_carol[0].body == greetings
    assert messages_to_carol[0].sender == adam