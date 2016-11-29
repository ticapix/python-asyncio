In C#

StartButton_Click event handler

async Task<int> AccessTheWebAsync() {
	HttpClient client = new HttpClient();

	Task<string> getStringTask = client.GetStringAsync('http://msdn.microsoft.com');

	DoIndependentWork();

	string urlContents = await getStringTask;
	return urlContents.Length;
}

void DoIndependentWork() {
	resultTextBox.Text += "Working ... \r\n";
}

Task<string> HttpClient.GetStringAsync(string url)

In Python
https://aiohttp.readthedocs.io/en/stable/

async def fetch(session, url):
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            return await response.text()

async def AccessTheWebAsync():

	getStringTask = fetch(session, 'http://msdn.microsoft.com')

	DoIndependentWork()

	async with aiohttp.ClientSession(loop=loop) as session:
        html = await getStringTask
        return len(html)

def DoIndependentWork():
	pass // some stuff
