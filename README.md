## About This Project

### Project Goals

The **Static Site Generator** project aims to provide a lightweight, customizable tool for generating static websites from Markdown content. This project is ideal for developers and content creators who want a streamlined and flexible way to create static websites without relying on complex frameworks or content management systems. The main goals of the project are to:

- **Simplify Static Site Creation**: Provide a straightforward tool for converting Markdown files into a fully functional static website.
- **Maintain High Customizability**: Allow users to define their templates and styles, enabling unique and personalized websites.
- **Ensure Easy Integration and Usage**: Offer a tool that can be easily integrated into existing workflows, supporting automation and customization.

### Key Features

- **Markdown to HTML Conversion**: Supports a wide range of Markdown elements (e.g., headings, lists, links, images) and converts them to clean HTML output.
- **Template-Based Rendering**: Users can define HTML templates that control the look and feel of the generated site, including placeholders for content, titles, and other dynamic elements.
- **Support for Common Markdown Elements**: Handles code blocks, inline code, blockquotes, ordered and unordered lists, bold, italic, links, and images, making content creation intuitive.
- **File-Based Content Management**: Automatically scans and processes Markdown files from a specified directory, organizing them into structured HTML pages.
- **Automated Page Generation**: Recursively generates HTML pages for each Markdown file found, ensuring that websites are generated quickly and efficiently.
- **Customizable Output**: Use CSS and JavaScript files to customize the design and interactivity of the generated static site.

### Technologies Used

- **Python**: The core language used for the static site generator, leveraging its powerful libraries and simplicity.
- **Regular Expressions (re)**: Utilized for parsing Markdown and identifying various syntaxes like bold, italics, links, and images.
- **Object-Oriented Programming (OOP)**: Utilizes classes and objects (e.g., `TextNode`, `HTMLNode`, `LeafNode`, `ParentNode`) to represent different HTML components and Markdown elements.
- **Unittest**: Python’s built-in testing framework is used to write comprehensive unit tests to ensure code reliability and correctness.
- **File Handling**: Efficient handling of file I/O operations to read Markdown files, process them, and generate corresponding HTML files.

### Learning Project

This project was developed as part of the **Boot.dev Backend Development Path**. It is a guided project designed to provide hands-on experience in building a static site generator from scratch using Python. The course description for this project reads:

> *"Ever wondered how SEO and performance-optimized static site generators like Hugo work? In this guided project you'll build your own from scratch using Python. You'll put a lot of your learnings from Object-Oriented Programming and Functional Programming to use in a tangible web project. This project isn't for the faint of heart, but it's well worth the effort. You'll come away with a deeper understanding of static content management."*

While the project was guided with pseudo-code and references to helpful Python documentation, **all the code was written by me**. I applied the concepts and built the functionality from scratch, allowing me to gain a deeper understanding of static content management and web development.
