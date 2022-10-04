import grpc

from definitions.builds.service_pb2 import Null, Ticket
from definitions.builds.service_pb2_grpc import TestServiceStub


def main():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)
        client.Health(Null())

        confirmation = client.AddTicket(
            Ticket(name="SomeTicket", description="...", story_points=2)
        )

        print(confirmation.expected_dateline)


if __name__ == "__main__":
    main()
