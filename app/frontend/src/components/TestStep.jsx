export default function TestStep({ step, index, updateStep, removeStep }) {
  return (
    <div className="flex gap-2 mb-2">
      <select
        className="border p-1"
        value={step.action}
        onChange={(e) => updateStep(index, 'action', e.target.value)}
      >
        <option value="goto">goto</option>
        <option value="fill">fill</option>
        <option value="click">click</option>
        <option value="expectUrl">expectUrl</option>
      </select>
      <input
        className="border p-1 flex-1"
        placeholder="Selector"
        value={step.selector}
        onChange={(e) => updateStep(index, 'selector', e.target.value)}
      />
      <input
        className="border p-1 flex-1"
        placeholder="Value"
        value={step.value}
        onChange={(e) => updateStep(index, 'value', e.target.value)}
      />
      <button className="bg-red-500 text-white px-2" onClick={() => removeStep(index)}>X</button>
    </div>
  );
}
