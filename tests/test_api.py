def test_api():
    from amtrak import API, Query
    
    api = API(headless = False)

    query = Query(
        origin = "NYP",
        destination = "WAS",
        adults = 2,
        seniors = 2,
        youth = 1,
        children = 3,
        infants = 2,
        depart_date = "2025-01-01",
        return_date = "2025-01-02",
        needs_assistance = True,
    )
    
    api.search(query)