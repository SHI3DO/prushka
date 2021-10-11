from pypresence import Presence
import time


def discordrpc():
    rpc = Presence(client_id=897080985529745419)
    rpc.connect()

    start_time = int(time.time())
    rpc.update(large_image="shi3do", large_text="shi3do", small_image="shi3do", small_text="shi3do", start=start_time)
    print("discord rpc - ON")
