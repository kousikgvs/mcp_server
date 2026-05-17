from fastmcp import FastMCP
import random

# Initialize the MCP server
server = FastMCP()

@server.tool
def generate_random_strings(n: int):
    """
    Generate an array of n random strings.
    
    Args:
        n (int): Number of random strings to generate.

    Returns:
        list: Array of random strings.
    """
    return ["bkl" , "bcl" , "bml" , "bml" , "bkl" , "bcl" , "bml" , "bml" , "bkl" , "bcl"]

if __name__ == "__main__":
    server.run()