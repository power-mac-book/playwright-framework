export default function TestControls({ runTest, saveTest }) {
  return (
    <div className="mt-4 flex gap-2">
      <button className="bg-green-500 text-white px-4 py-2" onClick={runTest}>Run Test</button>
      <button className="bg-gray-500 text-white px-4 py-2" onClick={saveTest}>Save Test</button>
    </div>
  );
}
