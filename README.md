# CRMOps
Technical test for CRM integration engineer position.

## Instructions to use.

Just change directory to `src` folder. then `python ./main.py`.

## Development details

### Service simulator
This exercise requires throwing request to a real server.
To avoid stressing server, we will develop a simulated service.
Before using this simulator, we need to make sure that this
simulator works exactly the same way that original service, so
that, we will write some tests to guarantee that.

To check all simulator-related tests are passed, just change
directory to `tests` and then `pytest test_service_simulator.py`.
This tests check normal and conflictive cases, comparing
simulated response with real response.

The advantage of using a simulator is that we will only throw
requests to the real service when everything is potentially working.

### Account Counter
This solution performs binary search algorithm, whose algoritmic
efficiency is $O(\log(n))$. To save some requests, solution 
implements a record system. It save record of the latest 
page visited, if it gave response
and the highest account: this let us know the count if that pages
are previous or next to the current, we don't need to revisit.