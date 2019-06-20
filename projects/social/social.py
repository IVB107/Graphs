
import random
import time

class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        # Add users
        for user in range(1, numUsers + 1):
            self.addUser(user)
        # Create friendships
        for i in range(0, (numUsers*avgFriendships)//2):
            rand_user = random.randint(1, numUsers)
            rand_friend = random.randint(1, numUsers)
            #  Ensure rand_user != rand_friend & that they are not already friends
            while (rand_user == rand_friend) or (rand_friend in self.friendships[rand_user] or rand_user in self.friendships[rand_friend]):
                # generate new rand_friend
                rand_friend = random.randint(1, numUsers - 1)
            # Add friendship
            self.addFriendship(rand_user, rand_friend)
                
        return self.friendships


    # def populateGraph(self, numUsers, avgFriendships):
    #     """
    #     Takes a number of users and an average number of friendships
    #     as arguments

    #     Creates that number of users and a randomly distributed friendships
    #     between those users.

    #     The number of users must be greater than the average number of friendships.
    #     """
    #     # Reset graph
    #     self.lastID = 0
    #     self.users = {}
    #     self.friendships = {}
    #     # !!!! IMPLEMENT ME

    #     # Add users
    #     # O(n)
    #     for i in range(numUsers):
    #         self.addUser(f"User {i + 1}")

    #     # Create friendships
    #     possibleFriendships = []
    #     # Time Complexity: O(n^2)
    #     for userID in self.users:
    #         for friendID in range(userID + 1, self.lastID + 1):
    #             possibleFriendships.append((userID, friendID))

    #     friendshipsToCreate = random.sample(possibleFriendships, (numUsers * avgFriendships) // 2)
    #     # numFriendshipsToCreate = (numUsers * avgFriendships) // 2
    #     # random.shuffle(possibleFriendships)
    #     # friendshipsToCreate = possibleFriendships[:numFriendshipsToCreate]
    #     for friendship in friendshipsToCreate:
    #         self.addFriendship(friendship[0], friendship[1])


    # def populateGraphLinear(self, numUsers, avgFriendships):
    #     # Reset graph
    #     self.lastID = 0
    #     self.users = {}
    #     self.friendships = {}
    #     # !!!! IMPLEMENT ME

    #     # Add users
    #     # O(n)
    #     for i in range(numUsers):
    #         self.addUser(f"User {i + 1}")

    #     targetFriendships = numUsers * avgFriendships
    #     totalFriendships = 0
    #     collisions = 0
    #     while totalFriendships < targetFriendships:
    #         userID = random.randint(1, self.lastID)
    #         friendID = random.randint(1, self.lastID)
    #         if self.addFriendship(userID, friendID):
    #             totalFriendships += 2
    #         else:
    #             collisions += 1
    #     print(f"COLLISIONS: {collisions}")

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        # Implement BFT
        visited = {}  # Note that this is a dictionary, not a set
        q = Queue()
        q.enqueue([userID])
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            # Skip users we've already visited
            if v not in visited:
                visited[v] = path
                for user in self.friendships[v]:
                    path_copy = list(path)
                    path_copy.append(user)
                    q.enqueue(path_copy)
        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    start_time = time.time()
    sg.populateGraph(50, 49)
    end_time = time.time()
    print(f'Runtime: {end_time - start_time} seconds')
    # print(sg.friendships)
    # connections = sg.getAllSocialPaths(1)
    # print(connections)
