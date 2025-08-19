export default function TestCaseList({ testCases, onChange }) {
  const handleDelete = async (id) => {
    await fetch(`http://localhost:8000/testcases/${id}`, { method: "DELETE" });
    onChange();
  };

  return (
    <div className="bg-white shadow rounded p-4">
      <h3 className="font-semibold mb-4">Test Cases</h3>
      {testCases.length === 0 ? (
        <p className="text-gray-500">No test cases yet.</p>
      ) : (
        <ul>
          {testCases.map((tc) => (
            <li key={tc.id} className="flex justify-between items-center border-b py-2">
              <div>
                <p className="font-medium">{tc.name}</p>
                <p className="text-sm text-gray-500">{tc.description}</p>
              </div>
              <button
                onClick={() => handleDelete(tc.id)}
                className="text-red-600 hover:underline"
              >
                Delete
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
