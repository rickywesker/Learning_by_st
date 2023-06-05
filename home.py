import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
st.header("Calculus📚")
st.subheader("What is This Website for?")
st.markdown(
    """
    Calculus has a lot of rules and formulas which are often presented as things to be memorized. Lots of derivative formulas, the product rule, the chain rule, implicit differentiation, the fact that integral and derivatives are opposite, Taylor series, just a lot of things like that. The goal of this website is for you to come away feeling like you could have invented calculus yourself that is cover all those core ideas.
    """
)
st.subheader("The area of a circle")
st.markdown("""
Maybe you know that this is pi times its radius squared. 
$$
S = \pi r^2
$$
But why? Is there a nice way to think about where this formula comes from?
Contemplating this problem and leaving yourself open to exploring the interesting thoughts that come about? 
Can actually lead you to a glimpse of three big ideas in calculus, **integrals, derivatives,
and the fact that they're opposites**.  



Let's say, with radius three, you're trying to figure out its area. Maybe you try out the idea of slicing up the circle into many concentric rings. 
""")
st.text('')
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image("images/circle.png",caption="Figure 1: A circle sliced into rings",width=300)

with col3:
    st.write(' ')

st.markdown("""
    Let's take one of those rings, 
which has some inner radius $r$ that's between zero and three. 
If we can find a nice expression for the area of each ring like this one, 
and if we have a nice way to add them all up, 
it might lead us to an understanding of the full circles area. 

""")
col11, col22, col33 = st.columns(3)
with col11:
    st.write(' ')

with col22:
    st.image("images/strip.png",caption="Figure 2: A ring sliced into a strip",width=300)

with col33:
    st.write(' ')

st.markdown("""For simplicity, let's just approximate it as a rectangle.
The width of that rectangle is the circumference of the original ring, 
which is $$2\pi r$$, and its thickness depends on how finely you chopped up the circle in the first place. In the spirit of using what will come to be
standard calculus notation. 
Let's call that thickness $dr$ for a tiny difference in the radius
from one ring to the next.  """)

st.markdown("""So the area of this ring is $$2\pi r dr$$, where $r=dr,2dr,3dr...$and if we add up all the rings, we get an approximation of the area of the circle. """)

opt = st.selectbox('Select the number of rings', [1,5,10,100,1000,10000,1000000,10000000,100000000])
ip = 3/opt
st.markdown(f"""The more rings we use, the better our approximation will be. Currently $dr$ = {ip}""")
area_approx = np.arange(0,3+ip,ip)
area_approx = np.sum(2*np.pi*area_approx*ip)

st.write("The area of the circle is theoratically ",np.pi*9,"square units")
st.write('The area of the circle is approximately ',area_approx,'square units')


def draw_ring(ax, center, radius, color):
    circle = plt.Circle(center, radius, fill=False, edgecolor=color, linewidth=0.2)
    ax.add_artist(circle)

# Create a new figure and set the same scale for both the x and y axis
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')

# Draw concentric circles centered at (0.5, 0.5) with given radii
draw_opt = opt
if draw_opt >= 1000:
    draw_opt = 1000
radii = np.arange(0, 3, 3/(draw_opt+2))
y = 2 * np.pi * radii
import plotly.express as px
barplot = px.bar(x=radii, y=y,labels={'x':'Radius','y':'Circumference'})


for i in radii:
    
    draw_ring(ax, (4, 4), i, 'blue')

# Set the x and y limits to include all the circles
ax.set_xlim(0, 8)
ax.set_ylim(0, 8)
# Set the x and y limits to include all the circles

col111, col222 = st.columns(2)
with col111:
    st.pyplot(fig)

with col222:
    st.plotly_chart(barplot)


