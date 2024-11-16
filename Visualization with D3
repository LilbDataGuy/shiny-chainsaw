# Introduction to the Data Visualization with D3 

D3.js, or D3, stands for Data Driven Documents. D3 is a JavaScript library to create dynamic and interactive data visualizations in the browser. It's built to work with common web standards, namely HTML, CSS, and Scalable Vector Graphics (SVG).

D3 takes input data and maps it into a visual representation of that data. It supports many different data formats. D3 lets you bind (or attach) the data to the Document Object Model (DOM). You use HTML or SVG elements with D3's built-in methods to transform the data into a visualization.


## 01- Add Document Elements with D3

```javascript
// selecting a dom element
const body = d3.select('body')


// appending elements to a node
const h1 = body.append('h1');


// setting text to the node
h1.text('Learing D3');


// Getting text from the node
const text = h1.text() // returns Learning D3
```



## 02- Select a Group of Elements

```javascript
// selectAll() is used to select a group of elements in the selected node
const anchor = d3.selectAll('a') // selects all anchor elements of the dom

body.selectAll('li')
    .text('list item');

```


## 03- Work with Data in D3

The first step is to make D3 aware of the data. The data() method is used on a selection of DOM elements to attach the data to those elements. The data set is passed as an argument to the method.

When enter() is combined with the data() method, it looks at the selected elements from the page and compares them to the number of data items in the set. If there are fewer elements than data items, it creates the missing elements.

1. select a group of elements with .selectAll
2. point dataset with .data(dataset)
3. chain .enter() methode to look for entries
4. append new elements with .append()

```javascript
// our data
const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

// append this data to a set of h2 tags
d3.selectAll('h2')      // select all h2 tags
    .data(dataset)      // point data to each h2 tag
    .enter()            // search for missing tags
    .append('h2')       // append missing tags
    // .text("New Title") // set the value of h2 tags to this text
```




## 04- Work with Dynamic Data in D3

The D3 text() method can take a string or a callback function as an argument:

```javascript
// selection.text((d) => d)

    .text( (d) => d + " USD")
```



## 05- Add Inline Styling to Elements

D3 lets you add inline CSS styles on dynamic elements with the style() method.

The style() method takes a comma-separated key-value pair as an argument. Here's an example to set the selection's text color to blue:

selection.style("color","blue");

```javascript
    // chage the style of all elements
    .style( "font-family", "verdana")
```


## 06-  Change Styles Based on Data

For example, you may want to color a data point blue if it has a value less than 20, and red otherwise. You can use a callback function in the style() method and include the conditional logic. 

```javascript
    .style( 'color', d => d < 20? 'red': 'green' )
```


## 07-  Add Classes with D3

Using a lot of inline styles on HTML elements gets hard to manage, even for smaller apps. It's easier to add a class to elements and style that class one time using CSS rules. D3 has the attr() method to add any HTML attribute to an element, including a class name.

The attr() method works the same way that style() does. It takes comma-separated values, and can use a callback function. Here's an example to add a class of "container" to a selection:

selection.attr("class", "container");

```javascript
    .attr('class', 'price')
```


## 08-  Update the Height of an Element Dynamically

The previous challenges covered how to display data from an array and how to add CSS classes. You can combine these lessons to create a simple bar chart. There are two steps to this:

1) Create a div for each data point in the array

2) Give each div a dynamic height, using a callback function in the style() method that sets height equal to the data value


```javascript
d3.selectAll('div')
    .data(dataset)
    .enter()
    .append('div')
    .attr('class', 'bar')
    .style('height', d =>  d + "px")
```


## 09-  Change the Presentation of a Bar Chart

1) Add space between each bar to visually separate them, which is done by adding a margin to the CSS for the bar class

2) Increase the height of the bars to better show the difference in values, which is done by multiplying the value by a number to scale the height

style.css
-------------
.bar {
    margin: 2px
}


```javascript
    .style('height', d => 10 * d + 'px')
```



## 10-  Learn About SVG in D3


SVG stands for Scalable Vector Graphics.

Here "scalable" means that, if you zoom in or out on an object, it would not appear pixelated. It scales with the display system, whether it's on a small mobile screen or a large TV monitor.

SVG is used to make common geometric shapes. Since D3 maps data into a visual representation, it uses SVG to create the shapes for the visualization. SVG shapes for a web page must go within an HTML svg tag.

```javascript
const svg = d3.select('body');
const w = 500, h = 100;

svg.append('svg')
    .attr('width', w)
    .attr('height', h)
```


## 11-  Display Shapes with SVG


There are a number of supported shapes in SVG, such as rectangles and circles. They are used to display data. For example, a rectangle (<rect>) SVG shape could create a bar in a bar chart.

When you place a shape into the svg area, you can specify where it goes with x and y coordinates. The origin point of (0, 0) is in the upper-left corner. Positive values for x push the shape to the right, and positive values for y push the shape down from the origin point.

```javascript
// Create a rect shape, and append it to svg element
// svg.append('rect')
//     // specify size of the rect
//     .attr('width', 25)
//     .attr('height', 100)

//     // set styles
//     .attr('fill', '#000')

//     // specify coordinates
//     .attr('x', 0)
//     .attr('y', 0)
```



## 12-  Create a Bar for Each Data Point in the Set


The rects must be appended to an svg element, not directly to the body. Also, you need to tell D3 where to place each rect within the svg area.

Use the data(), enter(), and append() methods to create and append a rect for each item in dataset.

```javascript
const dataset = [12, 31, 22, 17, 25, 18, 29, 14, 9];

// create a canvas
const canvas = d3.select('body')
    .append('svg')
    .attr('width', w)
    .attr('height', h)
    .attr('id', 'canvas')
    .style('background-color', '#f6f6f6')

// creat a rectangle for each data point of the array
const bars = canvas.selectAll('rect')

    .data(dataset)
    .enter()
    .append('rect')
```


## 13-  Dynamically Set the Coordinates for Each Bar


The placement of a rectangle is handled by the x and y attributes. They tell D3 where to start drawing the shape in the svg area. The last challenge set them each to 0, so every bar was placed in the upper-left corner.

For a bar chart, all of the bars should sit on the same vertical level, which means the y value stays the same (at 0) for all bars. The x value, however, needs to change as you add new bars. Remember that larger x values push items farther to the right. As you go through the array elements in dataset, the x value should increase.

The attr() method in D3 accepts a callback function to dynamically set that attribute. The callback function takes two arguments, one for the data point itself (usually d) and one for the index of the data point in the array. The second argument for the index is optional. Here's the format:

selection.attr("property", (d, i) => {
    d is the data point value
    i is the index of the data point in the array
})

It's important to note that you do NOT need to write a for loop or use forEach() to iterate over the items in the data set. Recall that the data() method parses the data set, and any method that's chained after data() is run once for each item in the data set.

```javascript
    .attr('x', ( d, i ) => i * 30 ) // multiply x coordinate by 30 each time
    .attr('y', 0)

    .attr('height', h)
    .attr('width', 25)
    .attr('fill', 'red')
```



## 14-  Dynamically Change the Height of Each Bar

Multiplying all data points by the same constant scales the data (like zooming in)
```javascript
    .attr('height', d => d * 3)
```



## 15-  Invert SVG Elements

The y coordinate that is y = heightOfSVG - heightOfBar would place the bars right-side-up.

Note: In general, the relationship is y = h - m * d, where m is the constant that scales the data points.

```javascript
    .attr('y', d => h - d * 3 )
```



## 16-  Change the Color of an SVG Elemen

In SVG, a rect shape is colored with the fill attribute. It supports hex codes, color names, and rgb values, as well as more complex options like gradients and transparency.

```javascript
    .attr('fill', 'navy')
```


## 17-  Add Labels to D3 Elements

D3 lets you label a graph element, such as a bar, using the SVG text element.

Like the rect element, a text element needs to have x and y attributes, to place it on the SVG canvas. It also needs to access the data to display those values.
```javascript
canvas.selectAll('text')
    .data(dataset)
    .enter()
    .append('text')


    // set the coordinates same as bars
    .attr('x', (d, i) => i * 30)
    .attr('y', d => h - d * 3 )

    .text( d => d)
    .style('font-size', 10)

```


## 18-  Style D3 Labels

D3 methods can add styles to the bar labels. The fill attribute sets the color of the text for a text node. The style() method sets CSS rules for other styles, such as "font-family" or "font-size".

```javascript
    .style('font-size', 12)
    .attr('fill', 'red')
```


## 19-  Add a Hover Effect to a D3 Element

It's possible to add effects that highlight a bar when the user hovers over it with the mouse. So far, the styling for the rectangles is applied with the built-in D3 and SVG methods, but you can use CSS as well.

```javascript
 bars.attr('class', 'bar')
```


## 20-  Add a Tooltip to a D3 Element

A tooltip shows more information about an item on a page when the user hovers over that item. There are several ways to add a tooltip to a visualization, this challenge uses the SVG title element.

```javascript
bars.append('title')
    .text( d => d)
```


## 21-  Create a Scatterplot with SVG Circles


A scatter plot is another type of visualization. It usually uses circles to map data points, which have two values each. These values tie to the x and y axes, and are used to position the circle in the visualization.

SVG has a circle tag to create the circle shape. It works a lot like the rect elements you used for the bar chart.

```javascript
const data = [
    [ 34,    78 ],
    [ 109,   280 ],
    [ 310,   120 ],
    [ 79,    411 ],
    [ 420,   220 ],
    [ 233,   145 ],
    [ 333,   96 ],
    [ 222,   333 ],
    [ 78,    320 ],
    [ 21,    123 ]
];

const w = 500, h = 500, r = 5;

// Main Canvas
const canvas = d3.select('body')
    .append('svg')
    .attr('width', w)
    .attr('height', h)
    .style('background-color', '#f6f6f6')

// Create Circles
const dots = canvas.selectAll('circle')
    .data(data)
    .enter()
    .append('circle')
```




## 22-  Add Attributes to the Circle Elements


A circle in SVG has three main attributes. The cx and cy attributes are the coordinates. They tell D3 where to position the center of the shape on the SVG canvas. The radius (r attribute) gives the size of the circle.

```javascript
// add cx, cy, radius attr to the circles

    .attr('cx', d => d[0])
    .attr('cy', d => h - d[1])
    .attr('r', r)
```


## 23-  Add Labels to Scatter Plot Circles


You can add text to create labels for the points in a scatter plot.

The goal is to display the comma-separated values for the first (x) and second (y) fields of each item in dataset.

The text nodes need x and y attributes to position it on the SVG canvas. In this challenge, the y value (which determines height) can use the same value that the circle uses for its cy attribute. The x value can be slightly larger than the cx value of the circle, so the label is visible. This will push the label to the right of the plotted point.

```javascript
const label = canvas.selectAll('text')

label.data(data)
    .enter()
    .append('text')

    // set x and y coordinates same as dots
    .attr('x', d => d[0] + 5) // add 5 points to x value to push text to the right
    .attr('y', d => h - d[1])
    .text( d => `${d[0]}, ${d[1]}`)
```


## 23-  Create a Linear Scale with D3


D3 has several scale types. For a linear scale (usually used with quantitative data), there is the D3 method scaleLinear():

`const scale = d3.scaleLinear()`

The idea of scaling is to fit max number of data into the rnage of the width and height of the canvas, for expample, let's say, how could you fit billion in a 500px width area, that is where the scale could help


```javascript
const scale = d3.scaleLinear();
const output = scale(50);

console.log(output);
```


## 24-  Set a Domain and a Range on a Scale


For sclaes we have to specify domain and range vlaues
.domain() takes an array of min and max - input value

.range() also takes an array of min and max - output value

```javascript
scale.domain([100, 500])
    .range([10, 50])


const color = d3.scaleLinear()

color.domain([-1, 0, 1])
    .range(["red", "white", 'green'])

console.log(color(-0.1)); // rgb(255, 230, 230)
```




## 25-  Use the d3.max and d3.min Functions to Find Minimum and Maximum Values in a Dataset



D3 has 2 methods to .min() and .max() to find the min and max values of the raw data

const exampleData = [34, 234, 73, 90, 6, 52];
d3.min(exampleData) // Returns 6
d3.max(exampleData) // Returns 234

these two methodes also take take callback functions as argument to specify wich point of data is being calculated

we can also use d3.extent() methode to find min and max values at once

```javascript
const positionData = [[1, 7, -4],[6, 3, 8],[2, 9, 3]]

// find the maximum of z value in the array
const zMax = d3.max(positionData, d => d[2]);
console.log(zMax);  // 8

// using extent() method
const exampleData = [34, 234, 73, 90, 6, 52];

const min_and_max = d3.extent(exampleData, d => d)

console.log(min_and_max);   // [6, 234]
```


## 26-  Use Dynamic Scales

the domain goes from 0 to the maximum in the set. It uses the max() method with a callback function based on the x values in the arrays. The range uses the SVG canvas' width (w), but it includes some padding, too. This puts space between the scatter plot dots and the edge of the SVG canvas.


```javascript
const dataset = [
    [ 34,    78 ],
    [ 109,   280 ],
    [ 310,   120 ],
    [ 79,    411 ],
    [ 420,   220 ],
    [ 233,   145 ],
    [ 333,   96 ],
    [ 222,   333 ],
    [ 78,    320 ],
    [ 21,    123 ]
];

const w = 500, h = 500, padding = 30

const xScale = d3.scaleLinear()
    .domain([0, d3.max(dataset, d => d[0])])
    .range([padding, w - padding]);

const yScale = d3.scaleLinear()
    .domain([0, d3.max(dataset, d => d[1])])
    .range([h - padding, padding])


// Define Axes
const xAxis = d3.axisBottom(xScale);
const yAxis = d3.axisLeft(yScale);

// create canvas
const canvas = d3.select('body').append('svg')

canvas.attr('width', w)
    .attr('height', h)
    .style('background-color', '#f9f9f9')


const dots = canvas.selectAll('circle')

dots.data(dataset)
    .enter()
    .append('circle')

    .attr('cx', d => xScale( d[0] ))
    .attr('cy', d => yScale( d[1] ))
    .attr('r', 5)


// Create labels
const label = canvas.selectAll('text');

label.data(dataset)
    .enter()
    .append('text')

    .attr('x', d => xScale( d[0] + 10))
    .attr('y', d => yScale( d[1] ))

    .text( d => `${d[0]}, ${d[1]}`)


canvas.append('g')
    .attr('transform', `translate(0, ${h - padding})`)
    .call(xAxis)

    canvas.append('g')
    .attr('transform', `translate(${padding}, 0)`)
    .call(yAxis)
