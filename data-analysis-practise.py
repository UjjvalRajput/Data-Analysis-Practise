import matplotlib.pyplot as plt
import pandas as pd

hollywood_actor_kills = pd.read_csv('actor_kill_counts.csv')
actor_names = hollywood_actor_kills['Actor'].values
kill_counts = hollywood_actor_kills['Count'].values

plt.barh(actor_names, kill_counts)
plt.title("actors kill counts")
plt.xlabel("Kill count")
plt.ylabel("Actors", rotation='horizontal')
plt.tight_layout()
plt.show()

import numpy as np

arcade_revenue_cs_doctorates = pd.read_csv(
    'arcade-revenue-vs-cs-doctorates.csv')
arcade_revenue = arcade_revenue_cs_doctorates[
    'Total Arcade Revenue (billions)'].values
cs_doctorates_awarded = arcade_revenue_cs_doctorates[
    'Computer Science Doctorates Awarded (US)'].values
x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
plt.scatter(x, arcade_revenue, color='green', s=np.pi * 3,
            alpha=0.5)
plt.scatter(x, cs_doctorates_awarded, color='red', s=np.pi * 3,
            alpha=0.5)
plt.title('Scatter plot')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
