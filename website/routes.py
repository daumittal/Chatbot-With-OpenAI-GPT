historyData = []
@routes.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        query = request.args.get('query')
        if query == "" or query is None:
            return render_template('response_view.html')
        response = ask(query)
        dataList = []
        queryMessage = Result(time="This Time", messagetype="other-message float-right", message=query)
        responseMessage = Result(time="This Time", messagetype="my-message", message=response)
        dataList.append(queryMessage)
        dataList.append(responseMessage)
        historyData.append(queryMessage)
        historyData.append(responseMessage)
        return render_template('response_view.html', results=dataList)
    else:
        return render_template('history.html', results=historyData)