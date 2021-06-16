import datetime
start=datetime.datetime.now()
end=datetime.datetime.now()
end.strftime("%Y-%m-%d-%H-%M-%S")

using_time_delta=(end-start)
using_time_delta.total_seconds()