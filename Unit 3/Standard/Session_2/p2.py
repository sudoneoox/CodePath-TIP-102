import heapq
from typing import List, Tuple


def process_performance_requests(requests):
    pq: List[Tuple] = []
    for request in requests:
        # negate so that the higher number has higher priority
        heapq.heappush(pq, (-request[0], request[-1]))

    pq = [ele[-1] for ele in pq]
    return pq


print(process_performance_requests([(3, "Dance"), (5, "Music"), (1, "Drama")]))
print(
    process_performance_requests(
        [(2, "Poetry"), (1, "Magic Show"), (4, "Concert"), (3, "Stand-up Comedy")]
    )
)
print(
    process_performance_requests(
        [
            (1, "Art Exhibition"),
            (3, "Film Screening"),
            (2, "Workshop"),
            (5, "Keynote Speech"),
            (4, "Panel Discussion"),
        ]
    )
)
