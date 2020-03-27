from asyncio.tasks import sleep
from datetime import datetime
import asyncio
import time

# for quick demonstration purposes, all non-paying users have the id of 1, paying users have the id of 2

time_threshold = 5 # seconds
number_of_rooms = 100
room_queues = {i+1: [] for i in range(number_of_rooms)}
rooms = {i+1: [1,1,1,1] for i in range(number_of_rooms)} # filling all rooms with 4 people
latest_entry_times = {i+1: datetime.now() for i in range(number_of_rooms)}


def queue_room_entry(user_id, room_id):
    total_people = len(rooms[room_id]) + len(room_queues[room_id])
    if total_people < 7:
        if user_id == 2:
            # find first occurrence of non-paying user in queue after the one waiting to be entered (paying users get to cut in line)
            insertion_point = room_queues[room_id][1:].index(1)
            room_queues[room_id].insert(insertion_point-1, 2)
        else:
            room_queues[room_id].append(1)
        return 'user queued for entry in room ' + str(room_id)
    return 'room '+ str(room_id) +' is full'


async def push_user_into_room(room_id):
    last_entry_time = latest_entry_times[room_id]
    time_difference = (datetime.now() - last_entry_time).total_seconds()
    if time_difference < time_threshold:
        await asyncio.sleep(time_threshold - time_difference)
    user = room_queues[room_id].pop(0)
    rooms[room_id].append(user)
    print('user '+ str(user) +' entered room ' + str(room_id))
    latest_entry_times[room_id] = datetime.now() # updating latest entry for the specified room


async def main():
    while True:
        for room_id, queue in room_queues.items():
            if len(queue) > 0:
                await push_user_into_room(room_id)


if __name__ == "__main__":
    print(queue_room_entry(1,2))
    print(queue_room_entry(1,2))
    print(queue_room_entry(2,2))
    print(queue_room_entry(1,2))
    print(queue_room_entry(1,3))
    print(queue_room_entry(1,3))
    print(queue_room_entry(2,3))
    print(queue_room_entry(1,3))
    asyncio.run(main())