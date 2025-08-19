export default function TestResult({ result }) {
  return (
    <div className="mt-4 p-2 border rounded bg-gray-50">
      <pre>{result}</pre>
    </div>
  );
}
