from collections import deque
# create an empty deque of aitel
Aitel_queue = deque()
print("===== enqueuing in Aitel client queue =====")
def aitel_enqueue(item):
    """ add an item to the end of the queue"""
    Aitel_queue.append(item)
    return f" enqueued client in Aitel queue {item} \n"

# after serve 1 client what is the next client to be served
def aitel_peek():
    """ peek at the front item of the queue without removing it"""
    if Aitel_queue: # check if there is any item
        remain = Aitel_queue.popleft()
        return f" The  client served is: {remain} \n"
    return "Queue is empty, nothing to peek"

# add an items
aitel_enqueue("Client 1")
aitel_enqueue("Client 2")
aitel_enqueue("Client 3")
aitel_enqueue("Client 4")
aitel_enqueue("Client 5")
print(Aitel_queue)
print(aitel_peek())
print(f" after served one client it remain: {Aitel_queue} \n")

# CHUK CHUK Queue
print("===== enqueuing in Chuk Chuk patient queue =====")
Chuk_patient_queue = deque()
def chuk_enqueue(item):
    """ add an item to the end of the queue"""
    Chuk_patient_queue.append(item)
    return f" enqueued patient in Chuk Chuk queue {item} \n"

# patient who served at third position
def chuk_serve_third():
    """ serve the third patient in the queue"""
    if len(Chuk_patient_queue) < 3:
        return "Not enough patients in the queue to serve the third one"
    served = Chuk_patient_queue[2]  # get the third patient (index 2)
    return f"The patient served at third position is: {served} \n"
# add an patients
chuk_enqueue("Patient 1")
chuk_enqueue("Patient 2")
chuk_enqueue("Patient 3")
chuk_enqueue("Patient 4")
chuk_enqueue("Patient 5")
chuk_enqueue("Patient 6")
chuk_enqueue("Patient 7")
chuk_enqueue("Patient 8")
chuk_enqueue("Patient 9")
print(Chuk_patient_queue)
print(chuk_serve_third())