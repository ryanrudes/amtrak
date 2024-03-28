from amtrak import Query

def test_query_validator():
    Query(
        origin = "NYP",
        destination = "WAS",
        adults = 2,
        children = 2,
        depart_date = "2025-01-01",
        return_date = "2025-01-02",
    )