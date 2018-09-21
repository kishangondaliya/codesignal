def pressureGauges(morning, evening):
    return [[min(e) for e in zip(morning, evening)],[max(e) for e in zip(morning, evening)] ]
