from GoogleNews import GoogleNews
import pandas as pd
gnews = GoogleNews(period='id')
gnews.search('Laboratorios Elea')
result = gnews.result()
data = pd.DataFrame.from_dict(result)
print(data)

data.to_html('noticias.html')