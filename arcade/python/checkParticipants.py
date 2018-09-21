def checkParticipants(participants):
    return [i for i, j in enumerate(participants) if j < i]
