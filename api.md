# ListStations

Types:

```python
from Amtrak_Rohit_Divate.types import ListStationListStationsResponse
```

Methods:

- <code title="get /stations">client.list_stations.<a href="./src/Amtrak_Rohit_Divate/resources/list_stations.py">list_stations</a>(\*\*<a href="src/Amtrak_Rohit_Divate/types/list_station_list_stations_params.py">params</a>) -> <a href="./src/Amtrak_Rohit_Divate/types/list_station_list_stations_response.py">ListStationListStationsResponse</a></code>

# ListTrips

Types:

```python
from Amtrak_Rohit_Divate.types import ListTripListTripsResponse
```

Methods:

- <code title="get /trips">client.list_trips.<a href="./src/Amtrak_Rohit_Divate/resources/list_trips.py">list_trips</a>(\*\*<a href="src/Amtrak_Rohit_Divate/types/list_trip_list_trips_params.py">params</a>) -> <a href="./src/Amtrak_Rohit_Divate/types/list_trip_list_trips_response.py">ListTripListTripsResponse</a></code>

# Bookings

Types:

```python
from Amtrak_Rohit_Divate.types import (
    Booking,
    BookingCreateResponse,
    BookingRetrieveResponse,
    BookingListResponse,
    BookingPayResponse,
)
```

Methods:

- <code title="post /bookings">client.bookings.<a href="./src/Amtrak_Rohit_Divate/resources/bookings.py">create</a>(\*\*<a href="src/Amtrak_Rohit_Divate/types/booking_create_params.py">params</a>) -> <a href="./src/Amtrak_Rohit_Divate/types/booking_create_response.py">BookingCreateResponse</a></code>
- <code title="get /bookings/{bookingId}">client.bookings.<a href="./src/Amtrak_Rohit_Divate/resources/bookings.py">retrieve</a>(booking_id) -> <a href="./src/Amtrak_Rohit_Divate/types/booking_retrieve_response.py">BookingRetrieveResponse</a></code>
- <code title="get /bookings">client.bookings.<a href="./src/Amtrak_Rohit_Divate/resources/bookings.py">list</a>(\*\*<a href="src/Amtrak_Rohit_Divate/types/booking_list_params.py">params</a>) -> <a href="./src/Amtrak_Rohit_Divate/types/booking_list_response.py">BookingListResponse</a></code>
- <code title="delete /bookings/{bookingId}">client.bookings.<a href="./src/Amtrak_Rohit_Divate/resources/bookings.py">delete</a>(booking_id) -> None</code>
- <code title="post /bookings/{bookingId}/payment">client.bookings.<a href="./src/Amtrak_Rohit_Divate/resources/bookings.py">pay</a>(booking_id, \*\*<a href="src/Amtrak_Rohit_Divate/types/booking_pay_params.py">params</a>) -> <a href="./src/Amtrak_Rohit_Divate/types/booking_pay_response.py">BookingPayResponse</a></code>

# WrapperCollection

Types:

```python
from Amtrak_Rohit_Divate.types import WrapperCollection
```

# LinksSelf

Types:

```python
from Amtrak_Rohit_Divate.types import LinksSelf
```

# LinksPagination

Types:

```python
from Amtrak_Rohit_Divate.types import LinksPagination
```
