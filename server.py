from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta

import grpc

from definitions.builds.service_pb2 import Calc_Result
from definitions.builds.service_pb2_grpc import (
    TestServiceServicer,
    add_TestServiceServicer_to_server,
)


class Service(TestServiceServicer):
    def Health(self, request, context):
        return request

    def AddTimeCalculation(self, request, context):
        calulation_result = datetime.utcnow() + timedelta(days=request.time_period)
        return Calc_Result(
            expected_dateline=calulation_result.strftime("%Y-%m-%d %H:%M:%S")
        )


def execute_server():
    server = grpc.server(ThreadPoolExecutor(max_workers=10))
    add_TestServiceServicer_to_server(Service(), server)
    server.add_insecure_port("[::]:3000")
    server.start()

    server.wait_for_termination()


if __name__ == "__main__":
    execute_server()
