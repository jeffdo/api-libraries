from dataclasses import dataclass
import re

QUERY_TEMPLATE = """mutation {{      
    getDatasetStatistics(
        input: {input_fields} 
    )
    {{        
        datasetStatisticsResponses {{
            {output_fields}      
        }}
    }}
}}
"""


def get_group(matchobj):
    if matchobj.group(2) == '':
        return matchobj.group(0)
    else:
        return matchobj.group(1) + matchobj.group(2)


def build_query(input_fields={}, output_fields=[]):
    # formatted_input = {key.replace('\'', ''): val for key, val in input_fields.items()}
    input_fields = re.sub("'(.*?)'(:?)", get_group, str(input_fields))
    input_fields = input_fields.replace("'", "\"")
    return QUERY_TEMPLATE.format(input_fields=input_fields, output_fields='\n\t'.join(output_fields))


@dataclass
class Input:
    """This class is not yet used in the API."""

    longitude: float
    latitude: float
    country: str
    city: str
    address: str
    warmingScenario: str
    datasetId: int

