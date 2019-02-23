import Choices from 'choices.js'

const ready = (runDefault) => {
  if (document.attachEvent ? document.readyState === 'complete' : document.readyState !== 'loading') {
    runDefault()
  } else {
    document.addEventListener('DOMContentLoaded', runDefault)
  }
}

ready(() => {
  const searchInput = new Choices(
    '.list-search',
    {
      searchPlaceholderValue: 'Type name',
      searchResultLimit: 5,
      itemSelectText: '',
    }
  )
  const typeFilterSelect = new Choices(
    '.type-filter',
    {
      maxItemCount: 4,
      placeholderValue: 'Filter by type (up to 4)',
    }
  )
  const resistanceFilterSelect = new Choices(
    '.resistance-filter',
    {
      maxItemCount: 6,
      placeholderValue: 'Filter by resistance (up to 6)',
    }
  )
  const superEffectivenessFilterSelect = new Choices(
    '.super-effectiveness-filter',
    {
      maxItemCount: 2,
      placeholderValue: 'Filter by super effectiveness (up to 2)',
    }
  )
  const pokemonListFilterWrapper = document.getElementById('pokemon-list-filter-wrapper')
  const searchPokemonWrapper = document.querySelector('.search-pokemon-wrapper')
  const moveTypeFilter = document.getElementById('move-type-filter')

  if (moveTypeFilter) {
    moveTypeFilter.addEventListener('change', event => {
      window.location = `${window.pgoURLs['list-url']}?selected-move-type=${event.currentTarget.value}`
    })
  }

  searchInput.passedElement.addEventListener('change', event => {
    window.location = `${window.pgoURLs['list-url']}${event.currentTarget.value}`
  })
  typeFilterSelect.passedElement.addEventListener('change', event => {
    const placeholder = typeFilterSelect.placeholder
    if (typeFilterSelect.passedElement.selectedOptions.length > 0) {
      typeFilterSelect.input.placeholder = ''
    } else {
      typeFilterSelect.input.placeholder = placeholder
    }
  })
  resistanceFilterSelect.passedElement.addEventListener('change', event => {
    const placeholder = resistanceFilterSelect.placeholder
    if (resistanceFilterSelect.passedElement.selectedOptions.length > 0) {
      resistanceFilterSelect.input.placeholder = ''
    } else {
      resistanceFilterSelect.input.placeholder = placeholder
    }
  })
  superEffectivenessFilterSelect.passedElement.addEventListener('change', event => {
    const placeholder = superEffectivenessFilterSelect.placeholder
    if (superEffectivenessFilterSelect.passedElement.selectedOptions.length > 0) {
      superEffectivenessFilterSelect.input.placeholder = ''
    } else {
      superEffectivenessFilterSelect.input.placeholder = placeholder
    }
  })

  const removePlaceholderIfSelected = () => {
    if (typeFilterSelect.passedElement.selectedOptions.length > 0) {
      typeFilterSelect.input.placeholder = ''
    }
    if (resistanceFilterSelect.passedElement.selectedOptions.length > 0) {
      resistanceFilterSelect.input.placeholder = ''
    }
    if (superEffectivenessFilterSelect.passedElement.selectedOptions.length > 0) {
      superEffectivenessFilterSelect.input.placeholder = ''
    }
  }

  removePlaceholderIfSelected()
  pokemonListFilterWrapper.hidden = false
  searchPokemonWrapper.hidden = false
})
