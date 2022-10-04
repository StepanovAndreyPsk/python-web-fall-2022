import grpc

from definitions.builds.service_pb2 import Null, Time_Calculation
from definitions.builds.service_pb2_grpc import TestServiceStub


def main():
    with grpc.insecure_channel("localhost:3000") as channel:
        client = TestServiceStub(channel)
        client.Health(Null())

        confirmation = client.AddTimeCalculation(
            Time_Calculation(name="SomeTicket", description="...", time_period=2)
        )

        print(confirmation.expected_dateline)


if __name__ == "__main__":
    main()
