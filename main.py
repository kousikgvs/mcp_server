from fastmcp import FastMCP
import random
import string

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
    def random_string():
        length = random.randint(5, 12)
        return ["bkl" , "bcl" , "bml" , "bklml"]

    return [random_string() for _ in range(n)]

if __name__ == "__main__":
    server.run(transport="streamable_http" , port=8000 , host="0.0.0.0")