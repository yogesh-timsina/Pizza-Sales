#styling for headers
def headerStyle(header):
    return f"""
    <div style='
    font-size: 2.2rem;
    font-weight: bold;
    font-family: cursive;
    color: #fff000;
    border: 1px solid #000fff;
    padding:5px 10px;
    text-align:center;
    margin: 20px 0;
    '>
        {header}
    </div>
"""

#style for KPI metrics
def kpiStyle(label:str, value:str):
    return f"""
    <div style='
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-bottom-left-radius: 5px;
    border-top-radius: 5px;
    margin: 10px 0;
    border: 1px solid #000fff;
    padding: 10px 20px;
    '>
        <div style='
        font-size: 1.5rem;
        font-weight: bold;
        '>
            {label}
        </div>
        <div style='
        font-size: 1.5rem;
        '>
            {value}
        </div>
    </div>
"""