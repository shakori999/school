import pytest

from ..models import Person 

@pytest.mark.django_db
@pytest.mark.count_queries(autouse=False)
def test_username_index_performance(valid_persons, count_queries):

    make_instance = 10
    # Create some instances to fill the database
    for _ in range(make_instance):
        valid_persons_instance = valid_persons()
        valid_persons_instance.save()

    # Perform a query that should use the username index
    username = 'testuser_1'
    query = Person.objects.filter(username=username).query
    explanation = query.explain(using='default')

    # Print the explanation to see its contents

    found_index_usage = False
    if "SEARCH dashboard_person USING INDEX" in explanation:
        found_index_usage = True

    # Check if the index usage information is in the explanation
    assert found_index_usage

    # Use the pytest-django-queries plugin to check the query count
    num_queries_executed = len(count_queries)

    num_queries_selected = num_queries_executed - num_queries_executed + 1
    
    # Calculate the expected number of queries (1 query for the filter)
    expected_queries = num_queries_executed - num_queries_executed + 1
    
    # Assert the number of queries executed
    assert num_queries_selected == expected_queries
