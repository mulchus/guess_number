from fastapi import FastAPI, Request

app = FastAPI()

numbers = {
    'max_number': 0,
    'hidden_number': 0,
    'guess_number': 0,
}


@app.get("/set_numbers/")
def set_numbers(request: Request):
    global numbers
    response = request.query_params
    numbers['max_number'] = int(response['max_number'])
    numbers['hidden_number'] = int(response['hidden_number'])
    if numbers['hidden_number'] > numbers['max_number']:
        return 'hidden_number must be less or equal than max_number'
    elif numbers['hidden_number'] < 0:
        return 'hidden_number must be greater or equal than 0'
    return {'numbers': numbers}


@app.get("/guess_number/{selected_number}")
def guess_number(selected_number):
    global numbers
    result = -1 if int(selected_number) > numbers['hidden_number'] else 1 if int(selected_number) < numbers[
        'hidden_number'] else 0
    if not result:
        numbers['guess_number'] = int(selected_number)
        return {'result': result, 'guess_number': numbers['guess_number']}
    return {'result': result}


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
