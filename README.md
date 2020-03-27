# room-filler

A simple app that shows queueing of multiple users to enter a specific room

# The question:

We have 100 chat rooms of a maximum of 7 users in progress. as new users come in we like to build a queue that can keep track of what time the most recent user joined the chat and wait at least 30 seconds till the next new user can join.

The queue will also put paid users ahead of the free users if rooms are about to get full.

# My solution:

I've utilised asyncIO to achieve this solution, ofcourse there are multiple ways to do it (such as Redis).
Users are represented as 1 or 2 (non-paying and paying respectively).
I've initialized 100 rooms with 4 users each and all the rooms have the same latest entry times set (datetime.now()).

When we execute the file, we try to insert 4 users each to rooms number 2 and 3 simultaneously. By default, we only allow a maximum of 7 users within a single room. So, the 4th user for both rooms is denied the possibility of entry.

Since the 3rd user being entered is a paying user, he gets to cut in line ahead of the 2nd user but not the first user. We don't want the first user to experience any sort of time increase on the front-end. The other non-paying users won't know if a paying user cut in line. Also, paying users don't cut ahead of other paying users.

The time interval between entries has been shortened to 5 seconds for easy visualisation, it can be easily modified by changing a constant at the top.

