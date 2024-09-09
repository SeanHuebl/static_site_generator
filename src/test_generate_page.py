import os
import tempfile
import unittest

from generate_page import extract_title, generate_page

class TestGeneratePage(unittest.TestCase):

    def setUp(self):
        """Set up temporary files for testing."""
        # Create a temporary directory for test files
        self.test_dir = tempfile.TemporaryDirectory()

        # Paths for temporary markdown and template files
        self.md_file_path = os.path.join(self.test_dir.name, 'index.md')
        self.template_file_path = os.path.join(self.test_dir.name, 'template.html')
        self.output_file_path = os.path.join(self.test_dir.name, 'output.html')

        # Write sample content to the temporary markdown file
        with open(self.md_file_path, 'w') as f:
            f.write("# This is a test title\n\nThis is a test content paragraph.")

        # Write sample content to the temporary template file
        with open(self.template_file_path, 'w') as f:
            f.write("<html><head><title>{{ Title }}</title></head><body>{{ Content }}</body></html>")

    def tearDown(self):
        """Clean up temporary files after testing."""
        self.test_dir.cleanup()

    def test_extract_title(self):
        """Test that `extract_title` correctly extracts a title from markdown content."""
        # Valid title extraction
        text = '# this is the title'
        self.assertEqual(extract_title(text), "this is the title")

        # Test that an exception is raised for content without a valid title
        text2 = 'this should throw an exception'
        with self.assertRaises(Exception):
            extract_title(text2)

    def test_generate_page(self):
        """Test that `generate_page` correctly generates an HTML file from markdown and a template."""
        # Generate page using temporary files
        generate_page(self.md_file_path, self.template_file_path, self.output_file_path)
        
        # Check that the output file was created
        self.assertTrue(os.path.exists(self.output_file_path))

        # Verify the content of the generated HTML file
        with open(self.output_file_path, 'r') as f:
            output_content = f.read()
        
        expected_content = "<html><head><title>This is a test title</title></head><body><div><h1>This is a test title</h1><p>This is a test content paragraph.</p></div></body></html>"
        self.assertEqual(output_content.strip(), expected_content)

if __name__ == "__main__":
    unittest.main()
